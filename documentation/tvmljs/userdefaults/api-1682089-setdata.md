# setData

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Stores the data for a given key.

**Availability**:
- tvOS 10.0+

## Declaration

```
void setData(
    in String key, 
    in String data
);
```

## Discussion

You can set the `data` parameter to `null` to remove the data associated with the key.

## Parameters

- `key`: The key for the data to be stored.
- `data`: The data to be stored.

## See Also

### Modifying User Defaults
- [getData](./api-1682084-getdata.md)
  Returns the data associated with a particular key.
- [removeData](./api-1682085-removedata.md)
  Removes the data associated with a particular key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/userdefaults/1682089-setdata)*