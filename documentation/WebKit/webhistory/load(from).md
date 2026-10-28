# load(from:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Loads the contents of the specified web history file.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func load(from URL: URL!) throws
```

```objc
- (BOOL) loadFromURL:(NSURL *) URL error:(NSError **) error;
```

## Discussion

When successful, this method posts a notification ([`WebHistoryLoadedNotification`](../webhistoryloadednotification.md)).

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `URL`: The URL of the file to load. The file should have been created previously by a web history object. Note that the file’s format is private and should not be edited directly.

## See Also

### Related Documentation
- [class func setOptionalShared(WebHistory!)](./setoptionalshared%28_%29.md)
  Sets the web history object to share.
- [class func optionalShared() -> WebHistory!](./optionalshared%28%29.md)
  Returns a shared web history object, if one exists.
### Loading and Saving History Information
- [func save(to: URL!) throws](./save%28to%29.md)
  Saves the web history to the specified file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webhistory/load(from:))*