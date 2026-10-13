class historyNode:
    def __init__(self, url, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev =prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.start = historyNode(homepage)
        self.curr = self.start

    def visit(self, url: str) -> None:
        visit =historyNode(url,None,self.curr)
        self.curr.next = visit
        self.curr = visit

    def back(self, steps: int) -> str:
        count = 0
        while self.curr.prev and count < steps:
            self.curr = self.curr.prev
            count += 1
        return self.curr.url


    def forward(self, steps: int) -> str:
        count = 0
        while self.curr.next and count < steps:
            self.curr = self.curr.next
            count += 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)