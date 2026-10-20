# setARxReqIntCompleteHandler

**Framework**: Kernel  
**Kind**: instm

Installs a callback to receive notification, when FWIM has completed ARxReqInt processing and no incoming packets are left in the queue.

## Declaration

```cpp
virtual void setARxReqIntCompleteHandler(
 void *refcon,
 IOFWARxReqIntCompleteHandlerhandler );
```

#### Return Value

none.

## Parameters

- `refcon`: Client's callback object.
- `handler`: Client callback to be invoked, at the end of interrupt processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspaceaux/1812922-setarxreqintcompletehandler)*