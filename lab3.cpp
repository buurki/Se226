#include <iostream>
using namespace std;

class Node {
public: 
    int data;
    Node *next;
    Node(int x) {
        data = x;
        next = nullptr;
    }
};

class Queue {
private:
    Node* front;
    Node* rear;
    int count;

public:
    Queue() : front(nullptr)
    ,rear(nullptr)
    ,count(0) {}

    void enqueue(int x) {
        Node* newNode = new Node(x);
        if (!rear) 
            front = rear = newNode;
        else {
            rear->next = newNode;
            rear = newNode;
        }
        count++;
    }

    void dequeue() { 
        if (isEmpty()) {
            return;
        }
        Node* temp = front;
        front = front->next;
        if (!front) 
            rear = nullptr;
        delete temp;
        count--;
    }

    int top() {
        return isEmpty() ? -1 : front->data;
    }

    bool isEmpty() {
        return front == nullptr;
    }

    int size() {
        return count;
    }

    ~Queue() {
        while (!isEmpty()) 
            dequeue();
    }
};

int main() {
    Queue q;
    q.enqueue(20);
    q.enqueue(5);
    q.enqueue(6);
    
    cout << "Front: " << q.top() << endl;  
    cout << "Size: " << q.size() << endl;  

    q.dequeue();
    cout << "Front : " << q.top() << endl;  
    cout << "Size: " << q.size() << endl;  

    return 0;
}
