console.log("Hello world");

function getApi1() {
    fetch("http://127.0.0.1:5000/dict").then((response) => response.json()).then((data) => {
        console.log(data);
        if(data.name) {
            document.getElementById("title").innerHTML = data.name;
        }
        if(data.data) {
            document.getElementById("content1").innerHTML = data.data;
        }
    })
}

function getApi2() {
    fetch("http://127.0.0.1:5000/").then((response) => response.json()).then((data) => {
        console.log(data);
        let count = data.count;
        console.log(count);
        let newContent = "";
        for(let i=0; i<count; i++) {
            newContent+= `
                <div>
                    <h3>Name: ${data.members[i].name} (${data.members[i].gradYear})</h3>
                    ${data.members[i].role}
                </div>
            `;
        }
        document.getElementById("content2").innerHTML = newContent;
    })
}