# Studying GITHUB

### Recap-1: What is git


GIT is a version-control software for code.

It is a commit DAG.


1. What is a commit? It is the current state of your code.

hash(_, content, meta) --> 1st-commit
hash(prev, content_n, meta) --> nth-commit
 

commitN - commitN-1 = delta(N-1) -> commit is the snapshot of the whole codebase.


2. Branch: It is just a pointer, which points to the hash of a commit (`commit* branch = commit;`)


U don't build any content, just create a new pointer. 

*MAIN* is exactly the same, just special.


`git branch some-branch` --> Creates a pointer which points to the current commit.


If you create new commits while in this branch, what happens is 
new commits are created, and at each new commit, the pointer `some-branch` points to the new one.


```
		__ E' <- F' <- G'
	       |	
	       v
A <- B <- C <- D <- E <- F


```

3. HEAD: Your location (your pointer).

Usually:

```

HEAD -> BRANCH -> COMMIT   # That is called the ATTACHED stated

```

This is nice, because when HEAD points to a branch, it points to a pointer which
updates with new commits.


If HEAD is detached (`git checkout hash-of-a-commit`), any commits will be added, but
will be orphan (as there is no branch pointer to update the commits from that 
point).






## COMMANDS: CHECKOUT VS RESET VS REVERT

1. CHECKOUT: Moves HEAD

```
git checkout abcdefg  # Move to commit abcdefg (or branch-pointer if branch name)

```

Just moving around, non-destructive.



2. RESET: Moves BRANCH


```
git reset c1  # Moves branch pointer to c1. 

```

Moving branch orphans the commits no longer contemplated by the branch


### MODES:

- `git reset --soft c1`
 
Moves branch only, keeps staging and working directory.
When you want to send N commits back as one.

- `git reset --mixed c1 # default`

Moves branch, clears staging, keeps working directory.
When you want to re-stage differently and maybe build in different commits.

- `git reset --hard c1 # `

Moves branch, clears staging area AND working directory - data loss POSSIBLE!!

UNCOMMITTED WORK GONE!!

Orphan commits are recoverable for a while if you know git secrets.

But again, UNCOMMITED WORK IS GONE FOR EVUR


3. revert - adds a new commit that undoes what previous commits did.

Useful when needs to undo stuff already pushed.

## Rebase and rewriting history.


```
      __ D
     |
A <- B <- C

```

Rebasing D to branch main (which points to C) 


```
      
     
A <- B <- C <- D'

```



Safety: `git reflog`

Shows where your HEAD has pointed recently, so you can find the hashes. 

Find a hash to the commit, create a branch pointing to it and there you go


`git branch recovery b2c3d4e # branch pointer "recovery" to commit`

 



