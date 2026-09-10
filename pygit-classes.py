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
        
        self.content = content.strip().lower[0] # Let us for now just take the first letter.
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
    branches: dict[Diff]

    def __init__(self) -> None:
        self.master = None
        self.branches = dict()

    def new_branch(self, branch_name: str, head: Diff) -> None:
        if not branch_name:
            raise ValueError("Branch must not be None")

        if not head:
            raise ValueError("HEAD points to null")

        diff = head
        branch = Branch(branch_name, diff)

        self.branches[branch_name] = branch

    def add_commit(self, diff: Diff, branch_name: str, head: Diff) -> None:
        if not diff:
            raise ValueError("Diff must not be None")

        if not branch_name:
            raise ValueError("Branch must not be None")

        branch_name = branch_name.lower().strip()
        branch = self.branches[branch_name]
        if not branch.get():
            raise Exception("There is no branch as")

        if branch.pointer != head:
            raise Exception("HEAD is DETACHED from branches. Not available for now.")

        # When commit is added, branch updates its pointer.
        diff.parents.append(branch.pointer)
        branch.pointer = diff




class DAGPrinter:
    commit_dag: CommitDAG

    def __init__(self, commit_dag: CommitDAG) -> None:
        self.commit_dag = commit_dag

    def print_dag(self) -> None:
        # For now only a list for I am tired son.

        dag = self.commit_dag
        for diff in dag:
            pass