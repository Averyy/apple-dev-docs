# Fixed Ordering Masks 1

**Framework**: Core Services

Set and test the `UCCollateOptions` field that specifies a fixed ordering scheme.

#### Overview

You can use these constants to set or obtain a value that specifies a fixed ordering scheme. For a description of the available types of fixed ordering schemes, see  [`Fixed Ordering Scheme`](carbon_core/unicode_utilities/1390361-fixed_ordering_scheme.md).

For example, to specify `kUCCollateTypeHFSExtended` in the `options` parameter of the function  [`UCCompareTextNoLocale(_:_:_:_:_:_:_:)`](1390513-uccomparetextnolocale.md) , the `kUCCollateTypeHFSExtended` value must be shifted by `kUCCollateTypeShiftBits ` :

`options = kUCCollateTypeHFSExtended     kUCCollateTypeShiftBits; `

You would obtain the ordering scheme value from the `options` parameter as follows:

```occ
fixedOrderType = ((options > > kUCCollateTypeShiftBits) &  kUCCollateTypeSourceMask);
```

See also [`Fixed Ordering Masks 2`](carbon_core/unicode_utilities/1390573-fixed_ordering_masks_2.md).

## Topics

### Constants
- [var kUCCollateTypeSourceMask: Int](kuccollatetypesourcemask.md)
  You can use this mask, in conjunction with the `kUCCollateTypeShiftBits` constant, to obtain a value identifying a fixed ordering scheme.
- [var kUCCollateTypeShiftBits: Int](kuccollatetypeshiftbits.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/unicode_utilities/1390370-fixed_ordering_masks_1)*