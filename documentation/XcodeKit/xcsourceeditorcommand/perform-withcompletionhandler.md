# perform(with:completionHandler:)

**Framework**: Xcodekit  
**Kind**: method  
**Required**: Yes

Performs the action associated with the command using the information in an invocation.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func perform(with invocation: XCSourceEditorCommandInvocation) async throws
```

## Mentions

- [Creating a Source Editor Extension](creating-a-source-editor-extension.md)
- [Testing Your Source Editor Extension](testing-your-source-editor-extension.md)

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func perform(with invocation: XCSourceEditorCommandInvocation) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func perform(with invocation: XCSourceEditorCommandInvocation) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Xcode passes the code a completion handler that it must invoke to finish performing the command, passing `nil` on success or an error on failure. A canceled command must still call the completion handler, passing `nil`.

There are no guarantees about the thread or queue on which the cancellation handler is invoked.

## Parameters

- `invocation`: The invocation of the command to be invoked.
- `completionHandler`: A block to be executed when the command finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommand/perform(with:completionhandler:))*