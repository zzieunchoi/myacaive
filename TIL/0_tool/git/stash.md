# git stash

git status를 보면 올리고 싶지 않은데 pull을 받기 위해서는 commit을 필수적으로 해야할 때가 있음 

그럴때 사용하는 stash!



## git stash 하기

```bash
$ git stash
Saved working directory and index state WIP on master: 451c825 Add index.html

$ git status 
On branch master
nothing to commit, working tree clean
```



## git stash 안에 있는거 빼기

```bash
$ git stash pop
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   README.md
    modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (1248c07e9784f15a5dfa8df78e50239fe083041f)

$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   README.md
    modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

