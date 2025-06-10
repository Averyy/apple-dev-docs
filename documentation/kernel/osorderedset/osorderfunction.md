# OSOrderFunction

**Framework**: Kernel  
**Kind**: tdef

The sorting function used by an OSOrderedSet to order objects.

## Declaration

```swift
typedef SInt32 ( *OSOrderFunction)(
   const OSMetaClassBase *obj1,
   const OSMetaClassBase *obj2,
   void *context);
```

#### Return_value

A comparison result of the object:

- a negative value if obj2 should precede obj1,
- a positive value if obj1 should precede obj2,
- and 0 if obj1 and obj2 have an equivalent ordering.

## Parameters

- `obj1`: An object from the ordered set. May be  .
- `obj2`: The object being ordered within the ordered set. May be  .
- `context`: A pointer to a user-provided context. May be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osorderedset/osorderfunction)*