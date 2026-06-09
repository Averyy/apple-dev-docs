# returnToQueue()

**Framework**: Virtualization  
**Kind**: method

Returns this element back to the guest.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func returnToQueue()
```

#### Discussion

Use this method when you are done processing this element and return it to the guest.

Use this method together with the [`nextElement()`](vzvirtioqueue/nextelement().md) method to process the elements in the queue.

The element you pass to this method must be one that you obtained from calling the [`nextElement()`](vzvirtioqueue/nextelement().md) method. Attempts to call this method more than once with the same element results in the framework raising an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueueelement/returntoqueue())*