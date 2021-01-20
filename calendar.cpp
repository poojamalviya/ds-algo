#include <bits/stdc++.h>
using namespace std;
static int randconunt = 1092020;

enum EventStatus {
    ACCEPTED=0,
    REJECTED,
    NOUPDATE
};

class RandomIdgenerator{
    const string key = "ajhjshjeebbebbejb$$772767272525336%%";
    static RandomIdgenerator* generator;
    RandomIdgenerator(){
        generator = NULL;
    }

    public:
        static RandomIdgenerator* getRandomIdgenerator(){
            if(generator)return generator;
            return new RandomIdgenerator();
        }

        static string generate() {
            return "ajhjshjeebbebbejb" + to_string(randconunt++);
        }
};

class User{
    private:
        string name;
        string userId;
    public:
        User(string bname):name(bname){
            userId = RandomIdgenerator::getRandomIdgenerator()->generate();
        }
        string getUserId(){
            return userId;
        }
        EventStatus notifyEvent(string eventId){
            return EventStatus::ACCEPTED;
        }
};

class Eventdata{
    protected:
        string startTime;
        string endTime;
        string ownerId;
        string locationId;
    public:
        Eventdata(string bStartTime,string bEndTime,string bownerid,string blocationid):
        startTime(bStartTime),
        endTime(bEndTime),
        ownerId(bownerid),
        locationId(blocationid){

                }
};

class Event{
    public :
        virtual vector<User*> getTargets()= 0 ;
    public:
        string getEventId(){
            return eventId;
        }
        string eventId;
};

class MeetingEvent: public Event{
    private:
        vector<User*> users;
        Eventdata* data;
    public:
        MeetingEvent(Eventdata* eventData){
            data =  eventData;
        }
        vector<User*> getTargets() {
            return users;
        }
};




class NotificationManager {
    private:
        void* cookie ;

    public :
        NotificationManager(void* bCookie) {
            cookie = bCookie;
        }

        vector<EventStatus> broadcastEvent(Event* event){
            vector<User*> users = event->getTargets();
            vector<EventStatus> userStatus(users.size(),EventStatus::NOUPDATE);
            for(int i=0;i<users.size();i++) {
                EventStatus status = users[i]->notifyEvent(event->getEventId());
                userStatus[i] = status;
            }
            return userStatus;
        }

};

class EventManager{
    map<string,Event*> events;
    map<string, map<string,EventStatus>> eventStatus;
    NotificationManager* ntfManager;

    public:
        EventManager(){
            ntfManager = new NotificationManager(this);
        }
        void addAEvent(Event* event) {
            events[event->getEventId()] = event ;
            vector<EventStatus> status = ntfManager->broadcastEvent(event);
            for(int i=0;i<event->getTargets().size();i++){
                eventStatus[event->getEventId()][event->getTargets()[i]->getUserId()] = status[i];
            }
        }

        map<string,EventStatus> getUserStatusForMeeting(string meetingId) {
            return eventStatus[meetingId];
        }
};



class EventCreator{
    EventManager* manager;
    static EventCreator* creator;
    EventCreator(){
        manager= new EventManager();
        creator = 0;
    }
    public:
        static EventCreator* getcreator(){
            if(!creator) return new EventCreator();
            return creator;
        }
    Event* createEvent(string type,Eventdata* eventData) {
        if(type == "meeting"){
            Event* event =  new MeetingEvent(eventData);
            manager->addAEvent(event);
            return event;
        }
    return 0;
    }
    EventManager* getManager(){
        return manager;
    } 
  
};



int main() {
    //create user
    User* user = new User("pooja");
    //create event through user
    EventCreator* creator = EventCreator::getcreator();
    Event* event = creator->createEvent("meeting", new Eventdata("1","2",user->getUserId(),"1224"));

    //3. Given a Meeting ID, provide an API to give details of invitees with their responses i.e., ACCEPT, DECLINE etc.
    creator->getManager()->getUserStatusForMeeting(event->getEventId());
    return 0;
}