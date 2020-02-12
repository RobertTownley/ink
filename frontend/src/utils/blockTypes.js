/* Array of block types available to the Ink Editor
 *
 * Blocks are sorted by default, with the `lead_order` field set to reflect
 * ordering of blocks within the "Lead Content" editor interface.
 */

const TextBlock = {
  block_type: "text",
  can_lead: true,
  default_value: {
    text: ""
  },
  label: "Text",
  icon: "mdi-format-text",
  lead_order: 2
};

const ImageBlock = {
  block_type: "image",
  can_lead: true,
  default_value: {
    alt_text: "",
    attribution: "",
    caption: "",
    image: {}
  },
  label: "Image",
  icon: "mdi-image",
  lead_order: 1
};

const EmbedBlock = {
  block_type: "embed",
  can_lead: true,
  default_value: {
    embedCode: ""
  },
  label: "Embed",
  icon: "mdi-code-tags",
  lead_order: 3
};

const CodeBlock = {
  block_type: "code",
  can_lead: true,
  default_value: {
    language: "",
    code: ""
  },
  label: "Code",
  icon: "mdi-code-braces",
  lead_order: 4
};

const PullQuoteBlock = {
  block_type: "pull_quote",
  can_lead: false,
  default_value: {
    quote: "",
    attribution: ""
  },
  label: "Pull Quote",
  icon: "mdi-comment-quote",
  lead_order: 5
};

const SectionHeaderBlock = {
  block_type: "section_header",
  can_lead: false,
  default_value: {
    anchor: "",
    header: ""
  },
  label: "Section Header",
  icon: "mdi-page-layout-header",
  lead_order: 6
};

const FeaturedLinkBlock = {
  block_type: "featured_link",
  can_lead: false,
  default_value: {
    href: "",
    text: "",
    target: "_blank"
  },
  label: "Featured Link",
  icon: "mdi-link",
  lead_order: 7
};

export function getBlockTypes() {
  return [
    TextBlock,
    ImageBlock,
    EmbedBlock,
    CodeBlock,
    PullQuoteBlock,
    SectionHeaderBlock,
    FeaturedLinkBlock
  ];
}
