const TOPIC1 = "hola!"
const TOPIC2 = "chau!"
const SLEEP = 1000

const zmq = require("zeromq")

async function run() {
    const sock = new zmq.Publisher

    await sock.bind("tcp://*:3000")
    console.log("Publisher iniciado!")

    let count = 0;

    while (true) {
        count++
        await sock.send([TOPIC1, count])
        await sock.send([TOPIC2, count])
        console.log(`Publicando mensaje #${count}, con el tópico ${TOPIC1}`)
        console.log(`Publicando mensaje #${count}, con el tópico ${TOPIC2}`)
        await new Promise(resolve => { setTimeout(resolve, SLEEP) })
    }
}

run()
