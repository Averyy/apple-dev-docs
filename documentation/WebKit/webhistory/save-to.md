# save(to:)

**Framework**: Webkit  
**Kind**: method

Saves the web history to the specified file.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func save(to URL: URL!) throws
```

#### Discussion

When successful, this method posts a notification ([`WebHistorySavedNotification`](webhistorysavednotification.md)).

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `URL`: The URL of the file to contain the web history information. The file must be user-writable, but its format is private and should not be edited directly.

## See Also

- [func load(from: URL!) throws](webhistory/load(from:).md)
  Loads the contents of the specified web history file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/save(to:))*