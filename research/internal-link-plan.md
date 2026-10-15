# Internal linking

Home links all four guides. Each article links the other three where relevant plus About for evidence policy. Beginner links the stamina heading in Combat; Mobile links the same section. Guides list, sidebar, related articles and tags use the template's actual content collection. Legal/footer navigation reaches all supporting pages. No links point to unpublished candidate pages.

Browser inspection discovered the template added a slash after fragment IDs. URL normalization now appends the trailing slash to the pathname only, preserving query and fragment targets. The regression test covers both cases.
