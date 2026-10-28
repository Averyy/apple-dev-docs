# setHidden(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Hides or shows the interface object in your user interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setHidden(_ hidden: Bool)
```

```objc
- (void) setHidden:(BOOL) hidden;
```

## Mentions

- [Connecting Your User Interface to Your Code](../connecting-your-user-interface-to-your-code.md)

## Discussion

When you hide or show an object in your interface, WatchKit makes a note to update the layout during the next refresh cycle. During that cycle, WatchKit adjusts the layout to display only the currently visible objects.

## Parameters

- `hidden`: A Boolean value indicating the visibility of the object. Specify [`true`](../../Swift/true.md) to hide the object. Specify [`false`](../../Swift/false.md) to show it.

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Hiding and Showing an Object
- [func setAlpha(CGFloat)](./setalpha%28_%29.md)
  Sets the opacity of the interface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sethidden(_:))*