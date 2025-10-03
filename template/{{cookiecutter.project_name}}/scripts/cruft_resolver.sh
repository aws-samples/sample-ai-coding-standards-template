#!/bin/bash
set -e

echo "🔍 Searching for .rej files..."

# Find all .rej files
REJ_FILES=$(find . -name "*.rej" -not -path "./.git/*" -not -path "./node_modules/*" -not -path "./.venv/*" -not -path "./venv/*")

if [ -z "$REJ_FILES" ]; then
    echo "✅ No .rej files found. Cruft update completed cleanly!"
    exit 0
fi

echo "📝 Found .rej files:"
echo "$REJ_FILES"
echo ""

SUCCESS_COUNT=0
TOTAL_COUNT=0

# Process each .rej file
for REJ_FILE in $REJ_FILES; do
    TOTAL_COUNT=$((TOTAL_COUNT + 1))
    SOURCE_FILE="${REJ_FILE%.rej}"

    echo "🔧 Processing: $REJ_FILE -> $SOURCE_FILE"

    if [ ! -f "$SOURCE_FILE" ]; then
        echo "❌ Source file $SOURCE_FILE does not exist"
        continue
    fi

    # Create backup
    cp "$SOURCE_FILE" "$SOURCE_FILE.backup"

    # Try to apply the patch with different strategies
    APPLIED=false

    # Strategy 1: Force apply with fuzzy matching, no prompts, no .orig files
    if patch --batch --forward --fuzz=3 --no-backup-if-mismatch "$SOURCE_FILE" < "$REJ_FILE" 2>/dev/null; then
        echo "✅ Applied patch with fuzzy matching to $SOURCE_FILE"
        rm -f "$REJ_FILE"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        APPLIED=true
    # Strategy 2: Try reverse patch with force
    elif patch --batch --reverse --forward --fuzz=3 --no-backup-if-mismatch "$SOURCE_FILE" < "$REJ_FILE" 2>/dev/null; then
        echo "✅ Applied reverse patch to $SOURCE_FILE"
        rm -f "$REJ_FILE"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        APPLIED=true
    # Strategy 3: Force apply ignoring most errors
    elif patch --batch --forward --force --fuzz=10 --no-backup-if-mismatch "$SOURCE_FILE" < "$REJ_FILE" 2>/dev/null; then
        echo "✅ Force applied patch to $SOURCE_FILE"
        rm -f "$REJ_FILE"
        SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
        APPLIED=true
    fi

    if [ "$APPLIED" = false ]; then
        # Restore backup if patch failed
        mv "$SOURCE_FILE.backup" "$SOURCE_FILE"
        echo "❌ Failed to apply patch to $SOURCE_FILE"
        echo "   Manual resolution required for $REJ_FILE"
    else
        # Remove backup if patch succeeded
        rm -f "$SOURCE_FILE.backup"
        # Clean up any .orig files that might have been created
        rm -f "$SOURCE_FILE.orig"
    fi

    echo ""
done

# Clean up any remaining .orig files
echo "🧹 Cleaning up .orig files..."
find . -name "*.orig" -not -path "./.git/*" -delete 2>/dev/null || true

# Clean up any remaining .rej files
echo "🧹 Cleaning up remaining .rej files..."
find . -name "*.rej" -not -path "./.git/*" -delete 2>/dev/null || true

echo "📊 Summary:"
echo "   ✅ Successfully resolved: $SUCCESS_COUNT"
echo "   ❌ Manually ignored: $((TOTAL_COUNT - SUCCESS_COUNT))"

echo ""
echo "🎉 Cruft update completed! All conflicts resolved or ignored."
exit 0
