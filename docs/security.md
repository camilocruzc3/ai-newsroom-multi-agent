# Security and privacy

## Public-repository boundary

Do not include private customer names, logos, identifiable emails, recipient lists, internal URLs, provider secrets, authentication tokens, operational logs, audio artifacts, published private newsletters, production prompts or client-specific business rules.

The public project starts with a separate Git history. Copying a private repository and deleting sensitive files from its current working tree would **not** remove those files from older commits.

## Runtime boundary (architecture guidance)

- Inject credentials through environment variables or a managed secret store.
- Separate local draft preparation from side-effecting delivery.
- Treat retrieved pages and documents as untrusted input, including prompt-injection attempts.
- Review source URLs before remote access and prevent unsafe redirect/network behavior.
- Validate recipient data and require authorization of the specific edition and audience.
- Limit logging of user, source and delivery data; define retention.
- Apply rate limits, concurrency controls, retries and idempotency where appropriate.
- Require independent assessment before real-world deployment.

## Rights and licensing

Sanitization alone does not prove that client-related source or visual assets may be republished. Confirm contractual, intellectual-property and workplace obligations before using screenshots or derived implementation material. MIT covers only this new public portfolio repository.

## Known boundary

No production security audit has been performed on this miniature public example; it does not send emails or make model/API calls.