# Bidirectional Character Values

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify bidirectional character properties.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kUCBidiCatNotApplicable](./api-1400035-bidirectional_character_values/kucbidicatnotapplicable.md)
  Unassigned.
- [kUCBidiCatLeftRight](./api-1400035-bidirectional_character_values/kucbidicatleftright.md)
  Strong types: L  left-to-right.
- [kUCBidiCatRightLeft](./api-1400035-bidirectional_character_values/kucbidicatrightleft.md)
  Strong types: R  right-to-left.
- [kUCBidiCatEuroNumber](./api-1400035-bidirectional_character_values/kucbidicateuronumber.md)
  Weak types: EN European number.
- [kUCBidiCatEuroNumberSeparator](./api-1400035-bidirectional_character_values/kucbidicateuronumberseparator.md)
  Weak types: ES European number separator.
- [kUCBidiCatEuroNumberTerminator](./api-1400035-bidirectional_character_values/kucbidicateuronumberterminator.md)
  Weak types: ET European number terminator.
- [kUCBidiCatArabicNumber](./api-1400035-bidirectional_character_values/kucbidicatarabicnumber.md)
  Weak types: AN Arabic number.
- [kUCBidiCatCommonNumberSeparator](./api-1400035-bidirectional_character_values/kucbidicatcommonnumberseparator.md)
  Weak types: CS common number separator.
- [kUCBidiCatBlockSeparator](./api-1400035-bidirectional_character_values/kucbidicatblockseparator.md)
  Separators: B  paragraph separator (was block separator).
- [kUCBidiCatSegmentSeparator](./api-1400035-bidirectional_character_values/kucbidicatsegmentseparator.md)
  Separators: S  segment separator.
- [kUCBidiCatWhitespace](./api-1400035-bidirectional_character_values/kucbidicatwhitespace.md)
  Neutrals: WS whitespace.
- [kUCBidiCatOtherNeutral](./api-1400035-bidirectional_character_values/kucbidicatotherneutral.md)
  Neutrals: ON other neutrals (unassigned codes could use this).
- [kUCBidiCatRightLeftArabic](./api-1400035-bidirectional_character_values/kucbidicatrightleftarabic.md)
  Unicode 3.0; AL right-to-left Arabic (was Arabic letter).
- [kUCBidiCatLeftRightEmbedding](./api-1400035-bidirectional_character_values/kucbidicatleftrightembedding.md)
  Unicode 3.0; LRE eft-to-right embedding.
- [kUCBidiCatRightLeftEmbedding](./api-1400035-bidirectional_character_values/kucbidicatrightleftembedding.md)
  Unicode 3.0; RLE right-to-left embedding.
- [kUCBidiCatLeftRightOverride](./api-1400035-bidirectional_character_values/kucbidicatleftrightoverride.md)
  Unicode 3.0; LRO left-to-right override.
- [kUCBidiCatRightLeftOverride](./api-1400035-bidirectional_character_values/kucbidicatrightleftoverride.md)
  Unicode 3.0; RLO right-to-left override.
- [kUCBidiCatPopDirectionalFormat](./api-1400035-bidirectional_character_values/kucbidicatpopdirectionalformat.md)
  Unicode 3.0; PDF pop directional Format.
- [kUCBidiCatNonSpacingMark](./api-1400035-bidirectional_character_values/kucbidicatnonspacingmark.md)
  Unicode 3.0; NSM non-spacing mark.
- [kUCBidiCatBoundaryNeutral](./api-1400035-bidirectional_character_values/kucbidicatboundaryneutral.md)
  Unicode 3.0; BN boundary neutral.
- [kUCBidiCatFirstStrongIsolate](./api-1400035-bidirectional_character_values/kucbidicatfirststrongisolate.md)
- [kUCBidiCatLeftRightIsolate](./api-1400035-bidirectional_character_values/kucbidicatleftrightisolate.md)
- [kUCBidiCatPopDirectionalIsolate](./api-1400035-bidirectional_character_values/kucbidicatpopdirectionalisolate.md)
- [kUCBidiCatRightLeftIsolate](./api-1400035-bidirectional_character_values/kucbidicatrightleftisolate.md)

## See Also

### Assorted Constants
- [Common and Special Unicode Values](./api-1400154-common_and_special_unicode_value.md)
  Specify sommon and special Unicode code values.
- [TEC Plugin Dispatch Table Versions](./api-1498348-tec_plugin_dispatch_table_versio.md)
  Specify a version for a TEC plug-in dispatch table.
- [TEC Plug-in Signatures](./api-1571831-tec_plug-in_signatures.md)
  Specify a TEC plug-in signature.
- [UCCharPropertyType](./uccharpropertytype.md)
  Specify property types for a Unicode charater.
- [UCCharPropertyValue](./uccharpropertyvalue.md)
  Specify a propery value for a Unicode character.
- [UnicodeMapVersion](./unicodemapversion.md)
  Specify a Unicode mapping version.
- [Unwanted Data Constants](./api-1400314-unwanted_data_constants.md)
  Specify data you don’t care about receiving.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1400035-bidirectional_character_values)*