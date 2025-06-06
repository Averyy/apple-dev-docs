# addObserver(_:)

**Framework**: Virtualization  
**Kind**: method

Adds an observer to notify about display configuration changes.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func addObserver(_ observer: any VZGraphicsDisplayObserver)
```

## Parameters

- `observer`: The new observer the framework notifies about display configuration changes.

## See Also

- [func removeObserver(any VZGraphicsDisplayObserver)](vzgraphicsdisplay/removeobserver(_:).md)
  Removes a display configuration change observer.
- [protocol VZGraphicsDisplayObserver](vzgraphicsdisplayobserver.md)
  A protocol you implement to observe state changes in graphic displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/addobserver(_:))*