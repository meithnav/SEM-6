#include <stdio.h>
#include <stdlib.h>


enum nodeColor{ BLACK , RED};

struct rbNode{
    int value, color;
    struct rbNode *parent;
    struct rbNode *link[2];
};


struct rbNode *root =NULL;

struct rbNode *createNode(int val){

    struct rbNode *newnode  ;  
    newnode = (struct rbNode *)malloc(sizeof(struct rbNode));
    newnode->value = val;
    newnode->parent=NULL;
    newnode->color = RED;
    newnode->link[0] = newnode->link[1] =NULL;
    return newnode;

}

void traversal(struct rbNode *node){

    // LVR
    if(node){
    char color;
    traversal(node->link[0]);
    color = node->color == BLACK? 'B':'R';
    printf(" %d%c ", node->value , color);
    traversal(node->link[1]);

    }
    
}


void LLRotation(struct rbNode *ptr , struct rbNode *parent , struct rbNode *greatParent){

    int index = greatParent->parent->link[0]== greatParent ? 0:1 ;
    greatParent->parent->link[index]= parent;
    parent->parent= greatParent->parent;
    greatParent->parent=parent;
    parent->link[1] = greatParent;

}

void RRRotation(struct rbNode *ptr , struct rbNode *parent , struct rbNode *greatParent){

   int index = greatParent->parent->link[0]== greatParent ? 0:1 ;
    greatParent->parent->link[index]= parent;
    parent->parent= greatParent->parent;
    greatParent->parent=parent;
    parent->link[0] = greatParent;

}

void checkConflict(struct rbNode *ptr , struct rbNode *parent , struct rbNode *parentSibling){

    if(parent->color ==RED){

        // CASE 1: SIBLING BLACK 
        if(parentSibling->color == BLACK){
            int ptrEdge, parentEdge ;
            ptrEdge = parent->link[0] == ptr? 0:1;
            parentEdge = parent->parent->link[0] == parent? 0:1;

            if(parentEdge==0 && ptrEdge==0){
                // LL
                printf("LL CONFLICT");
                LLRotation(ptr , parent, parent->parent);

            }else if(parentEdge==1 && ptrEdge==1){
                // RR
                printf("RR CONFLICT");
                 RRRotation(ptr , parent, parent->parent);

            }else if(parentEdge==0 && ptrEdge==1){
                // LR
                printf("LR CONFLICT");
                struct rbNode *greatparent = parent->parent;
                greatparent->link[0]= ptr;
                ptr->parent = greatparent ;
                ptr->link[0]= parent;
                parent->parent = ptr;
                parent->link[1]=ptr->link[0];
                LLRotation(ptr , parent, greatparent);

            }else {
                // RL
                printf("RL CONFLICT");
                struct rbNode *greatparent = parent->parent;
                greatparent->link[1]= ptr;
                ptr->parent = greatparent ;
                ptr->link[1]= parent;
                parent->parent = ptr;
                parent->link[0]=ptr->link[1];
                RRRotation(ptr , parent, greatparent);

            }
        

        }else if(parentSibling->color == RED){
            // CASE 2: SIBLING RED
            parentSibling->color=BLACK;
            parent->color=BLACK;
            if(parent->parent != root){
                // printf("RECHECK PARENT's PARENT");
                parent->parent->color = parent->parent->color ==RED? BLACK : RED;
                // find new ptr
                ptr =  parent->parent;
                parent = ptr->parent;
                parentSibling = parent->link[0] == ptr? parent->link[1]:parent->link[0] ;
                checkConflict(ptr, parent ,parentSibling);
            }

        }

    }
}


void insertion(int data){

    struct rbNode *newnode , *ptr, *parent, *sibling, *parentSibling;
    int index , sibIndex;

    printf("\n\nAFTER INSERTION %d:  ", data)  ;
    newnode = createNode(data);
    if(!root){
        root = newnode;
        root->color= BLACK;
        traversal(root);
        return;
    }

    // SEARCH
    ptr = root;
    while(ptr !=NULL){

        if(ptr->value == data){
            printf("  DUPLICATES NOT ALLOWED!");
            return;
        }

        index = ptr->value - data > 0? 0:1 ;
        sibIndex = ptr->value - data > 0? 1:0 ;

        parentSibling =sibling ;
        parent = ptr ;
        sibling = ptr->link[sibIndex];
        ptr = ptr ->link[index];

    }

    // ADD
    parent->link[index]= newnode;
    newnode->parent =parent;
    ptr=newnode;

    printf("\nPARENT : %d ,  ", parent->value);
    
    if(parentSibling==NULL){
        printf("PARENT'S SIBLING : NULL  " );
    }else{
    printf("PARENT'S SIBLING : %d   ", parentSibling->value);
    }

    // CHECK FOR CONFLICTS
    checkConflict(ptr, parent ,parentSibling);


    printf("\nTREE :");
    traversal(root);
}



int main(){

    insertion(10);
    insertion(18);
    insertion(7);
    insertion(15);
    insertion(99);
    insertion(16);


    printf("\n\n");



    return 0; 
}
