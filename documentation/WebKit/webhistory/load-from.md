# load(from:)

**Framework**: WebKit  
**Kind**: method

Loads the contents of the specified web history file.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func load(from URL: URL!) throws
```

#### Discussion

When successful, this method posts a notification ([`WebHistoryLoadedNotification`](webhistoryloadednotification.md)).

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `URL`: The URL of the file to load. The file should have been created previously by a web history object. Note that the file’s format is private and should not be edited directly.

## See Also

- [class func setOptionalShared(WebHistory!)](webhistory/setoptionalshared(_:).md)
  Sets the web history object to share.
- [class func optionalShared() -> WebHistory!](webhistory/optionalshared.md)
  Returns a shared web history object, if one exists.
- [func save(to: URL!) throws](webhistory/save(to:).md)
  Saves the web history to the specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/load(from:))*