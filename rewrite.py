import re

with open('templates/my_tasks.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_main = '''<main class="relative pt-16 bg-surface min-h-screen p-space-xl">
<div class="flex flex-col w-full">
<div class="mb-space-xl flex items-center justify-between">
    <div>
        <h2 class="text-headline-md font-headline-md text-on-surface mb-space-xs">My Tasks</h2>
        <p class="text-body-md text-on-surface-variant">Manage and track your assigned work.</p>
    </div>
</div>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-space-md">
    {% for task in tasks %}
    <div class="bg-surface-container-lowest rounded-2xl p-space-lg shadow-[0_4px_12px_rgba(0,0,0,0.02)] border border-surface-container hover:shadow-[0_8px_24px_rgba(0,0,0,0.06)] hover:border-primary/20 transition-all cursor-pointer group flex flex-col justify-between">
        <div>
            <div class="flex items-center justify-between mb-space-md">
                <div class="flex items-center gap-space-sm">
                    <span class="material-symbols-outlined text-tertiary text-[20px]">task</span>
                    <span class="text-label-sm font-medium text-tertiary uppercase tracking-wider">Task</span>
                </div>
            </div>
            <h3 class="text-headline-xs font-headline-xs text-on-surface mb-space-xs group-hover:text-primary transition-colors">{{ task.title }}</h3>
            <p class="text-body-sm text-on-surface-variant mb-space-md">Due: {{ task.deadline }} | {{ task.hours_estimated }} hrs</p>
        </div>
        <div>
            <span class="px-space-sm py-1 bg-secondary-container text-on-secondary-container rounded-full text-label-sm font-medium">{{ task.status }}</span>
        </div>
    </div>
    {% else %}
    <div class="col-span-full py-10 text-center text-on-surface-variant">
      <p>No tasks assigned to you right now.</p>
    </div>
    {% endfor %}
</div>
</div>
</main>'''

content = re.sub(r'<main.*?</main>', new_main, content, flags=re.DOTALL)

with open('templates/my_tasks.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('templates/analytics.html', 'r', encoding='utf-8') as f:
    content2 = f.read()

new_main2 = '''<main class="relative pt-16 bg-surface min-h-screen p-space-xl">
<div class="flex flex-col w-full">
<div class="mb-space-xl flex items-center justify-between">
    <div>
        <h2 class="text-headline-md font-headline-md text-on-surface mb-space-xs">Analytics</h2>
        <p class="text-body-md text-on-surface-variant">Overview of organizational performance.</p>
    </div>
</div>

<div class="bg-surface-container-lowest rounded-2xl p-space-lg shadow-[0_4px_12px_rgba(0,0,0,0.02)] border border-surface-container">
    <div class="py-20 text-center text-on-surface-variant">
        <span class="material-symbols-outlined text-[48px] mb-space-sm text-outline-variant">monitoring</span>
        <h3 class="text-headline-sm font-headline-sm text-on-surface mb-space-xs">Analytics Dashboard</h3>
        <p>This page is currently under development. Detailed charts and velocity metrics will appear here.</p>
    </div>
</div>
</div>
</main>'''

content2 = re.sub(r'<main.*?</main>', new_main2, content2, flags=re.DOTALL)

with open('templates/analytics.html', 'w', encoding='utf-8') as f:
    f.write(content2)
