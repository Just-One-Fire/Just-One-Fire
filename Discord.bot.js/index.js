const Discord = require('discord.js');
const ping = require("./Events/message.js")
const client = new Discord.Client();


client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

module.exports.execute = (client, message) => {
  if (message.author.bot) return;
  if (!message.content.startsWith($)) return;

  let command = message.content.split(" ")[0];
  command = command.slice(prefix.length);

  let args = message.content.split(" ").slice(1);

  // if(command === "ping"){
  //     message.reply('Pong');
  //     console.log("ok");
  // }
  const args = 'ping';
  switch (args) {
    case 'ping':
    case 'Ping':
        return ping(commande, args, message);
    
}
};

client.login("Njc5NzY0Mjg1NTA4OTQ0MDY3.XlfqMA.YQ5D8tV9appezrwQNYUyCQzqkdk")