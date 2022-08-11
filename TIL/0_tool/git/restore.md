# git restore

현재 내 변경사항!

```bash
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        restore.md
        stash.md

nothing added to commit but untracked files present (use "git add" to track)
```



그리고 git add를 해서 stage에 옮김

```bash
$ git add .
```



그러면 restore.md와 stash.md가 모두 넘어간다!



앗 갑자기 restore.md를 unstaged 하고 싶다면?

```bash
$ git restore --staged restore.md
```

하고 다시 $ git status를 찍어본다면

```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   stash.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        restore.md
```



그리고 다시 넣고 싶으면 git add 사용!