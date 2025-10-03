/* Custom JavaScript for {{cookiecutter.project_name}} Documentation */

document.addEventListener('DOMContentLoaded', function() {
    // Add copy button functionality for code blocks
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(function(codeBlock) {
        const pre = codeBlock.parentNode;
        if (pre.querySelector('.copy-button')) return; // Already has copy button

        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.textContent = 'Copy';
        copyButton.style.cssText = `
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            padding: 0.25rem 0.5rem;
            background: var(--md-primary-fg-color);
            color: white;
            border: none;
            border-radius: 0.25rem;
            cursor: pointer;
            font-size: 0.75rem;
            opacity: 0.7;
            transition: opacity 0.2s;
        `;

        pre.style.position = 'relative';
        pre.appendChild(copyButton);

        copyButton.addEventListener('click', function() {
            navigator.clipboard.writeText(codeBlock.textContent).then(function() {
                copyButton.textContent = 'Copied!';
                setTimeout(function() {
                    copyButton.textContent = 'Copy';
                }, 2000);
            });
        });

        copyButton.addEventListener('mouseenter', function() {
            copyButton.style.opacity = '1';
        });

        copyButton.addEventListener('mouseleave', function() {
            copyButton.style.opacity = '0.7';
        });
    });

    // Add smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Update URL without jumping
                history.pushState(null, null, '#' + targetId);
            }
        });
    });

    // Add architecture layer indicators
    const architectureHeaders = document.querySelectorAll('h2, h3');
    architectureHeaders.forEach(function(header) {
        const text = header.textContent.toLowerCase();
        let layerClass = '';

        if (text.includes('infrastructure') || text.includes('stack') || text.includes('script')) {
            layerClass = 'infrastructure-layer';
        } else if (text.includes('function') || text.includes('handler')) {
            layerClass = 'functions-layer';
        } else if (text.includes('domain') || text.includes('model') || text.includes('service')) {
            layerClass = 'domain-layer';
        } else if (text.includes('port') || text.includes('interface')) {
            layerClass = 'ports-layer';
        } else if (text.includes('adapter') || text.includes('integration')) {
            layerClass = 'adapters-layer';
        } else if (text.includes('test')) {
            layerClass = 'tests-layer';
        }

        if (layerClass) {
            header.classList.add('architecture-layer', layerClass);
        }
    });

    // Enhance search functionality
    const searchInput = document.querySelector('input[data-md-component="search-query"]');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();

            // Add search suggestions based on architecture layers
            if (query.includes('infra')) {
                console.log('Searching in Infrastructure layer...');
            } else if (query.includes('func')) {
                console.log('Searching in Functions layer...');
            } else if (query.includes('domain')) {
                console.log('Searching in Domain layer...');
            } else if (query.includes('port')) {
                console.log('Searching in Ports layer...');
            } else if (query.includes('adapter')) {
                console.log('Searching in Adapters layer...');
            } else if (query.includes('test')) {
                console.log('Searching in Tests layer...');
            }
        });
    }
});

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('input[data-md-component="search-query"]');
        if (searchInput) {
            searchInput.focus();
        }
    }

    // Escape to close search
    if (e.key === 'Escape') {
        const searchInput = document.querySelector('input[data-md-component="search-query"]');
        if (searchInput && document.activeElement === searchInput) {
            searchInput.blur();
        }
    }
});
