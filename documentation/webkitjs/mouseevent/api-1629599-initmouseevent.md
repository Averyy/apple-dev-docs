# initMouseEvent

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- Safari Desktop 3.0+
- Safari Mobile 1.0+

## Declaration

*Safari Desktop*

```
void initMouseEvent(
    optional DOMString type, 
    optional boolean canBubble, 
    optional boolean cancelable, 
    optional DOMWindow? view, 
    optional long detail, 
    optional long screenX, 
    optional long screenY, 
    optional long clientX, 
    optional long clientY, 
    optional boolean ctrlKey, 
    optional boolean altKey, 
    optional boolean shiftKey, 
    optional boolean metaKey, 
    optional unsigned short button, 
    optional any relatedTarget
);
```

*Safari Mobile*

```
void initMouseEvent(
    optional DOMString type, 
    optional boolean canBubble, 
    optional boolean cancelable, 
    optional DOMWindow? view, 
    optional long detail, 
    optional long screenX, 
    optional long screenY, 
    optional long clientX, 
    optional long clientY, 
    optional boolean ctrlKey, 
    optional boolean altKey, 
    optional boolean shiftKey, 
    optional boolean metaKey, 
    optional unsigned short button, 
    optional EventTarget? relatedTarget
);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/mouseevent/1629599-initmouseevent)*