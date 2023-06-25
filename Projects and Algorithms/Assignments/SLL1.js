class Node {
    constructor(data) {
        this.data = data;
        this.next = null;              
    }
}
class SLL {
    constructor() {
        this.head = null;
    }
    addFront(val) {
        let new_node = new Node(val);
        if(!this.head) {
            this.head = new_node;
            return this;
        }
        new_node.next = this.head;
        this.head = new_node;
        return this;
    }
    removeFront(){
        if (!this.head){
            return null;
        }
        this.head = this.head.next;
        return this;
    }
    front(){
        if (!this.head){
            return null;
        }
        return this.head.data;
    }
    displayValues(){
        let runner = this.head
        let values = "";
        while (runner != null){
            if (runner == this.head){
                values+= runner.data;
            }
            else{
                values+=", " + runner.data;
            }
            runner = runner.next
        }
        return values;
    }
}

SLL1 = new SLL();
console.log(SLL1);
SLL1.addFront(18);
console.log(SLL1);
SLL1.addFront(5);
console.log(SLL1);
SLL1.addFront(73);
console.log(SLL1);
console.log("1- ", SLL1.displayValues());
SLL1.removeFront();
console.log("2- ", SLL1.displayValues());
SLL1.addFront(100);
console.log("3- ", SLL1.displayValues());
SLL1.addFront(11.41);
console.log("4- ", SLL1.displayValues());


