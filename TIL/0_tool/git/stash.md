# git stash

<<<<<<< HEAD
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
=======
아직 마무리하지 않은 작업을 스택에 잠시 저장할 수 있도록 하는 명령어이다. 이를 통해 아직 완료하지 않은 일을 commit하지 않고 나중에 다시 꺼내와 마무리할 수 있다.



## stash

```bash
$ git status
Changes to be committed:
(use "git reset HEAD <file>..." to unstage)
modified:   index.html
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)
modified:   lib/simplegit.rb
```



## stash 목록 확인

```bash
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```



## stash에 있는 것 빼오기

```bash
// 가장 최근의 stash를 가져와 적용한다.
$ git stash apply
// stash 이름(ex. stash@{2})에 해당하는 stash를 적용한다.
$ git stash apply [stash 이름]

// Staged 상태까지 저장
$ git stash apply --index
>>>>>>> 532ab7b4955e459c06381460564f925618e3ed44
```

