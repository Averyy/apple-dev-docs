# initMouseEvent(_:canBubble:cancelable:view:detail:screenX:screenY:clientX:clientY:ctrlKey:altKey:shiftKey:metaKey:button:relatedTarget:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

## Declaration

```swift
func initMouseEvent(_ type: String!, canBubble: Bool, cancelable: Bool, view: DOMAbstractView!, detail: Int32, screenX: Int32, screenY: Int32, clientX: Int32, clientY: Int32, ctrlKey: Bool, altKey: Bool, shiftKey: Bool, metaKey: Bool, button: UInt16, relatedTarget: (any DOMEventTarget)!)
```

```objc
- (void) initMouseEvent:(NSString *) type canBubble:(BOOL) canBubble cancelable:(BOOL) cancelable view:(DOMAbstractView *) view detail:(int) detail screenX:(int) screenX screenY:(int) screenY clientX:(int) clientX clientY:(int) clientY ctrlKey:(BOOL) ctrlKey altKey:(BOOL) altKey shiftKey:(BOOL) shiftKey metaKey:(BOOL) metaKey button:(unsigned short) button relatedTarget:(id<DOMEventTarget>) relatedTarget;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/dommouseevent/initmouseevent(_:canbubble:cancelable:view:detail:screenx:screeny:clientx:clienty:ctrlkey:altkey:shiftkey:metakey:button:relatedtarget:))*