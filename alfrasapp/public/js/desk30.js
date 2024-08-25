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
            frappe.call({
                method: 'alfrasapp.config.controller.get_workspaces',
                callback: function(response) {
                    let workspaces = response.message;
                    let root_pages = {};

                    workspaces.forEach(workspace => {
                        if (!workspace.parent_page) {
                            root_pages[workspace.name] = {
                                title: workspace.title,
                                url: `/app/${generateSlug(workspace.name)}`,
                                children: {}
                            };
                        } else {
                            if (!root_pages[workspace.parent_page]) {
                                root_pages[workspace.parent_page] = {
                                    title: workspace.parent_page,
                                    url: `/app/${generateSlug(workspace.parent_page)}`,
                                    children: {}
                                };
                            }
                            root_pages[workspace.parent_page].children[workspace.name] = {
                                title: workspace.title,
                                url: `/app/${generateSlug(workspace.name)}`
                            };
                        }
                    });

                    Object.keys(root_pages).forEach(key => {
                        build_top_menu_section(root_pages[key].title, root_pages[key].children);
                    });
                }
            });

            let sidebarMenu = document.querySelector('.sidebar-menu');
            if (sidebarMenu) {
                sidebarMenu.style.display = 'none';
            }
        }, 1000);
    });
});
