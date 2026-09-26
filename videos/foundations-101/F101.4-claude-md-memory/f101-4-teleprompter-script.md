Welcome to the Analytics AI Enablement education series. Today in Foundations, we focus on Claude dot M D and auto memory.

If you've used Claude Code for a while, you've probably seen a file called Claude dot M D, and wondered whether you're supposed to do something with it.

It's a short note Claude reads at the start of every session, so you don't have to repeat yourself. It's also easy to overfill.

When Anthropic released Opus 5, the Claude Code team deleted about eighty percent of its own system prompt. That's the set of instructions Claude gets before you type anything. The new model didn't need most of them.

Your file works the same way. You don't need a rule for every situation. Claude handles most everyday work without detailed instructions, and every line takes up room in its context.

Use it for things Claude can't work out on its own. Tell it which files to leave alone, which commands not to run, and where the source of truth lives. And if you've corrected Claude on the same thing twice, and it'll keep coming up, write it down.

For most work, you'll use one of three places.

Your personal file follows you into every project on your machine. Put your own working style there, such as keep answers short, or no pie charts. Our course guideline is under a hundred lines.

A project file lives in the folder your team shares. Table locations and metric definitions go there. If your team counts annual wellness visit completion one particular way, write that down, so Claude doesn't have to guess.

A file inside a subfolder only kicks in when Claude opens files in that folder, so a Snowflake rule stays out of the way until the work touches Snowflake.

Claude combines the files it has loaded, and one doesn't replace another. If two files disagree, Claude could follow either one. Remove the rule that's out of date. If both are still right, reword them to say when each one applies.

The file guides Claude, but it doesn't enforce anything. It won't block an action or make an answer right, so you still check the work.

You may also have seen Claude say it saved a memory. That's auto memory. Unlike Claude dot M D, Claude writes these notes itself, and they stay on your machine. It's on by default and mostly takes care of itself. If you spot a note that's wrong, fix it. If it looks right, you don't need to do anything.

Now try it. Think of one rule you've had to explain to Claude more than once, and write it as one specific line. "Never modify the source export" is specific. "Be careful with the data" isn't.

Type slash memory, and choose your personal file if the rule is just for you, or the project file if it's for your team. Paste the line in. To check it worked, start a new session, type slash context, and look for your file on the list.

Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing channel so we can improve the course.
