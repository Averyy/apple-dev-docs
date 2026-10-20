# save(to:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Saves the web history to the specified file.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func save(to URL: URL!) throws
```

```objc
- (BOOL) saveToURL:(NSURL *) URL error:(NSError **) error;
```

#### Discussion

When successful, this method posts a notification ([`WebHistorySavedNotification`](../webhistorysavednotification.md)).

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `URL`: The URL of the file to contain the web history information. The file must be user-writable, but its format is private and should not be edited directly.

## See Also

### Loading and Saving History Information
- [func load(from: URL!) throws](./load%28from%29.md)
  Loads the contents of the specified web history file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/save(to:))*