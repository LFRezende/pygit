# PyGit classes 
# from hashlib import Sha --> Claude fucked me up to the point of this

class Diff:
    content: str
    parents: list['Diff']

    def __init__(self, content: str , parents: list['Diff']) -> None:
        if not content:
            return

        if not parents:
            raise ValueError("Diff must have parents")
        
        self.content = content
        self.parents = parents 


class Branch:
    def __init__(self, name: str, diff: Diff):
        if not name:
            raise ValueError("No name for branch")

        if not diff:
            raise ValueError("Branch must point to diff")

        self.name = name
        self.pointer = diff


class CommitDAG:
    master: Diff | None
    branches: list[Diff]

    def __init__(self):
        self.master = None
        self.branches = list()

    def new_branch(self):
        pass