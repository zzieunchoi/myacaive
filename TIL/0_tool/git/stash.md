# git stash

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
```

