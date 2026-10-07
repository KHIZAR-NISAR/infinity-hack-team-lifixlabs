with open('templates/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add ID to form
content = content.replace('<form method="POST" action="{{ url_for(\'process_transcript\') }}">', '<form id="transcript-form" method="POST" action="{{ url_for(\'process_transcript\') }}">')

# Add loading spinner and change button text class
content = content.replace('Generate Projects with AI', '<span id="btn-text">Generate Projects with AI</span><svg id="btn-spinner" class="hidden animate-spin ml-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>')

# Add JS and Toast HTML
js_html = '''
<!-- Toast Notification -->
<div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2"></div>

<script>
function showToast(message, isError=false) {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `flex items-center gap-3 px-4 py-3 rounded-xl shadow-lg transform transition-all duration-300 translate-y-10 opacity-0 ${isError ? 'bg-error-container text-on-error-container border border-error/20' : 'bg-primary-container text-on-primary-container border border-primary/20'}`;
    toast.innerHTML = `
        <span class="material-symbols-outlined text-[20px]">${isError ? 'error' : 'check_circle'}</span>
        <p class="text-body-md font-medium">${message}</p>
    `;
    container.appendChild(toast);
    
    // Animate in
    setTimeout(() => {
        toast.classList.remove('translate-y-10', 'opacity-0');
    }, 10);
    
    // Remove after 3s
    setTimeout(() => {
        toast.classList.add('opacity-0');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

const form = document.getElementById('transcript-form');
if (form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const btnText = document.getElementById('btn-text');
        const btnSpinner = document.getElementById('btn-spinner');
        const submitBtn = form.querySelector('button[type="submit"]');
        
        // Loading state
        submitBtn.disabled = true;
        submitBtn.classList.add('opacity-70', 'cursor-not-allowed');
        btnText.textContent = 'Processing...';
        btnSpinner.classList.remove('hidden');
        
        try {
            const formData = new FormData(form);
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            
            if (response.ok && data.success) {
                showToast('Projects and Tasks generated successfully!');
                setTimeout(() => window.location.reload(), 1500);
            } else {
                showToast(data.error || 'An error occurred processing the transcript.', true);
                // Reset state
                submitBtn.disabled = false;
                submitBtn.classList.remove('opacity-70', 'cursor-not-allowed');
                btnText.textContent = 'Generate Projects with AI';
                btnSpinner.classList.add('hidden');
            }
        } catch (err) {
            showToast('Network error or server unavailable.', true);
            submitBtn.disabled = false;
            submitBtn.classList.remove('opacity-70', 'cursor-not-allowed');
            btnText.textContent = 'Generate Projects with AI';
            btnSpinner.classList.add('hidden');
        }
    });
}
</script>
</body>'''

content = content.replace('</body>', js_html)

with open('templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)
