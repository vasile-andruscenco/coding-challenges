"""
https://leetcode.com/problems/simplify-path/

Pattern:
    Stack

Given an absolute Unix-style path that always begins with a slash '/', returns its
simplified canonical path.

Unix path rules:
- a single period '.' refers to the current directory,
- a double period '..' refers to the parent directory,
- multiple consecutive slashes ('//', '///') count as a single slash '/',
- any other sequence of periods ('...', '....') is a valid directory or file name.

The canonical path must:
- start with a single slash '/',
- separate directories by exactly one slash '/',
- not end with a trailing slash unless it is the root,
- contain no '.' or '..' components.

Args:
    path (str): A valid absolute Unix path consisting of English letters, digits,
        '.', '/' or '_'.

Returns:
    str: The simplified canonical path.

Examples:
    simplifyPath("/home/")
    "/home"

    simplifyPath("/home//foo/")
    "/home/foo"

    simplifyPath("/home/user/Documents/../Pictures")
    "/home/user/Pictures"

    simplifyPath("/../")
    "/"

    simplifyPath("/.../a/../b/c/../d/./")
    "/.../b/d"

Constraints:
    - 1 <= len(path) <= 3000
    - path consists of English letters, digits, '.', '/' or '_'.
    - path is a valid absolute Unix path.
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


solution = Solution()

path = "/.../a/../b/c/../d/./"

print("Input:", path)
print("Canonical:", solution.simplifyPath(path))  # Output: "/.../b/d"
