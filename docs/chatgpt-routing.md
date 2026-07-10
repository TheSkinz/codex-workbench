# ChatGPT Adapter

The ChatGPT layer is intentionally thin. It makes a good routing and synthesis decision, creates a portable task packet, and evaluates evidence returned by the execution surface. It does not become a second knowledge base.

## Install in ChatGPT

Use the contents of `chatgpt/PROJECT-INSTRUCTIONS.md` as the instructions for your existing AI-workflow Project. Add `chatgpt/TASK-PACKET-TEMPLATE.md` as a project file if you want the exact format available in every thread.

Do not create a second generic harness Project. Keep domain work in its own bounded project or in the canonical repository/vault that already governs it.

## Minimal operating loop

1. Bring the request to ChatGPT.
2. ChatGPT selects a route and writes a task packet.
3. Send the packet to Codex, Deep Research, GitHub, or another explicit execution surface.
4. Return the resulting artifact, diff, source links, or test output.
5. Ask ChatGPT to perform final evidence-based QA and produce the next handoff.

## Tool selection rules

| Situation | Use | Avoid |
|---|---|---|
| Current local repository state | Codex or GitHub read | Memory-only claims |
| Public, current, consequential facts | Deep Research | Uncited model recall |
| A bounded implementation with validation | Codex | Browser-first manual work |
| A GitHub repository, branch, PR, or commit | GitHub | Recreating state from pasted summaries |
| Connected private data | Specific connected app | Uploading broad data sets unnecessarily |
| One-off browser interaction | Agent Mode | Turning it into unattended authority |

## Decision boundary

Use ChatGPT to decide **what should happen and what would prove it happened**. Use the execution surface to perform the work. Keep the final evidence with the durable artifact, not only in chat.
