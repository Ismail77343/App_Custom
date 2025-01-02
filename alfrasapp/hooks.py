from . import __version__ as app_version

app_name = "alfrasapp"
app_title = "Alfrasapp"
app_publisher = "ismail haimi"
app_description = "Alfrasapp"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "himiismail123@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = ["/assets/alfrasapp/css/desk66.css","/assets/alfrasapp/css/chatGpt11.css"]
app_include_js = ["/assets/alfrasapp/js/desk63.js","/assets/alfrasapp/js/gpt146.js","/assets/alfrasapp/js/chatGpt51.js"]


# app_include_js = [
#     "/assets/js/login.js"
# ]

# website_route_rules = [
#     {"from_route": "/login", "to_route": "login"}
# ]

# Installation
# ------------
after_install = "alfrasapp.install.after_install_tasks"

# Uninstallation
# ------------
# before_uninstall = "alfrasapp.uninstall.before_uninstall"
# after_uninstall = "alfrasapp.uninstall.after_uninstall"

# Document Events
# ---------------
# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# 
# Testing
# -------
# before_tests = "alfrasapp.install.before_tests"

# Scheduled Tasks
# ---------------
# scheduler_events = {
#	"all": [
#		"alfrasapp.tasks.all"
#	],
#	"daily": [
#		"alfrasapp.tasks.daily"
#	],
#	"hourly": [
#		"alfrasapp.tasks.hourly"
#	],
#	"weekly": [
#		"alfrasapp.tasks.weekly"
#	],
#	"monthly": [
#		"alfrasapp.tasks.monthly"
#	]
# }

# Fixtures
# --------
fixtures = [
    {
        "doctype": "Print Format",
        "filters": [
            ["name", "in", ["Alfras Pos Invoic"]]
        ]
    }
]

# Authentication and authorization
# --------------------------------
# auth_hooks = [
#	"alfrasapp.auth.validate"
# ]
