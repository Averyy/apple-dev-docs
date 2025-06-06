# removeObserver(_:)

**Framework**: Virtualization  
**Kind**: method

Removes a display configuration change observer.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func removeObserver(_ observer: any VZGraphicsDisplayObserver)
```

## Parameters

- `observer`: The observer to remove from notifications about display configuration changes.

## See Also

- [func addObserver(any VZGraphicsDisplayObserver)](vzgraphicsdisplay/addobserver(_:).md)
  Adds an observer to notify about display configuration changes.
- [protocol VZGraphicsDisplayObserver](vzgraphicsdisplayobserver.md)
  A protocol you implement to observe state changes in graphic displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/removeobserver(_:))*