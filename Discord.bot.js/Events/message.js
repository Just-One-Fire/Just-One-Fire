module.exports.execute = (client, message) => {
    if (message.author.bot) return;
    if (!message.content.startsWith($)) return;

    let command = message.content.split(" ")[0];
    command = command.slice(prefix.length);

    let args = message.content.split(" ").slice(1);

    if(command === "ping"){
        message.reply('Pong');
        console.log("ok");
    }
};