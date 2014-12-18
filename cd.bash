function cd() {
  new_directory="$*";

  if [ $# -eq 0 ]; then 
      new_directory=${HOME};
  fi;

  builtin cd "${new_directory}" && /home/andrew/dev/python/cd_git_branch/cd_git.py
}
