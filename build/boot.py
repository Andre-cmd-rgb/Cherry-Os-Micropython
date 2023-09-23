import senko

OTA = senko.Senko(
  user="Andre-cmd-rgb", # Required
  repo="Cherry-Os-Micropython", # Required
  branch="main", # Optional: Defaults to "master"
  working_dir="build", # Optional: Defaults to "app"
  files = ["test.txt"]
)