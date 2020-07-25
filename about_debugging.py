class AboutDebugging:

    def bug_source_one(self):
        foo = "bar"
        foo += 1

    def bug_source_two(self):
        pass


if __name__ == '__main__':
    AboutDebugging.bug_source_one(AboutDebugging)