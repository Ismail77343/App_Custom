function build_top_menu_section(title, root_pages) {
    let top_menu_section = $(
        `<div class="top-menu-section dropdown" data-title="${title}">
            <button class="btn-reset top-menu-label dropdown-toggle" data-toggle="dropdown">
                <span class="section-title">${__(title)}</span>
            </button>
            <div class="dropdown-menu"></div>
        </div>`
    );

    prepare_top_menu(root_pages, top_menu_section);

    let header = document.querySelector('.navbar');
    if (header) {
        header.appendChild(top_menu_section[0]);
    }
}

function prepare_top_menu(root_pages, top_menu_section) {
    let menu_items = top_menu_section.find('.dropdown-menu');

    workspaces.forEach(workspace => {
        if (!workspace.parent_page) {
            // أنشئ عنصر القائمة الأب
            let parentMenuItem = $('<li class="parent-menu-item"></li>');
            let link = $(`<a href="/app/${generateSlug(workspace.title)}">${workspace.title}</a>`);
            parentMenuItem.append(link);

            // أنشئ قائمة فرعية (dropdown) إذا كان لديه أبناء
            let childMenu = $('<ul class="child-menu"></ul>');

            workspaces.forEach(child => {
                if (child.parent_page === workspace.name) {
                    let childLink = $(`<a href="/app/${generateSlug(child.title)}">${child.title}</a>`);
                    childMenu.append($('<li></li>').append(childLink));
                }
            });

            if (childMenu.children().length > 0) {
                parentMenuItem.append(childMenu);
                parentMenuItem.addClass('has-children');
            }

            topMenu.append(parentMenuItem);
        }
    });
}

function generateSlug(title) {
    return title.toLowerCase().replace(/\s+/g, '-').replace(/[^\w\-]+/g, '').replace(/\-\-+/g, '-');
}

frappe.after_ajax(function() {
    $(document).ready(function() {
        setTimeout(function() {
 // حذف الـ header الافتراضي
            $path=document.getElementById("navbar-breadcrumbs");
            $nav=document.getElementsByClassName("sticky-top")[0];
            $nav.appendChild($path);
        }, 1000);
    });
});
