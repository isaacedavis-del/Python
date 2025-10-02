arrow = [
    "    *    ",
    "   * *   ",
    "  *   *  ",
    " *     * ",
    "***   ***",
    "  *   *  ",
    "  *   *  ",
    "  *****  ",
    ""
    ]

arrow_formatted= []
for item in arrow:
    line = f"{item} {item}"
    arrow_formatted.append(line)

arrow_print = "\n".join(arrow_formatted)

print(arrow_print)