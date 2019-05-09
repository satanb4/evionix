def articles():
    articles = [
        {
            'id':1,
            'author':'Gaatha Bhatia',
            'title':'The Eklavya Vision',
            'body':"""It is a widely known fact that availability of good quality, affordable healthcare services is scarce in India. One of the major sections of society comprises of upper limb amputees, be it our brave soldiers returning from war after serving the country, or the common man who succumbed to a disease, and even unfortunate children, who lose a part of their childhood along with it. According to the latest statistics, India houses more than 12 million upper limb (Hand) amputees. Most of the amputees belong to low income and/or lower middle-class background and cannot afford ultra-expensive prosthetic extension or hand, many amputees are reported to land into depression and undergo trauma due to the loss of limb. Therefore, there is always need and demand for cheap and reliable prosthetic's and is a recurring market.
                    Thus, we aim to do our part by helping solve this problem by introducing Eklavya, which is a fully functional active bionic hand being developed keeping in mind the lower income groups and making it as affordable as possible. What is unique about Eklavya is not only the functionality it offers in its price range, but also the fact that it will be made in a modular fashion. Each component will be replaceable with ease and will allow the user to swap out for a replacement in case there is any malfunction of components. This will be made possible due to the high efficiency of the manufacturing methods which allow the prices to be pushed down in bulk quantities. This will be an active device with electronics that are embedded into the product. This allows for the device to be capable of doing a multitude of functions with the help of software. There is a one-size fits all design decision to allow the device to be accessible to everyone regardless of the amputation type and also curtail the medical costs.
                    As of now, the solutions which are present, are provided by the larger companies. These companies charge a much larger amount and thus are not accessible to the lower end economic segment. There are also exclusive channels through which these companies are providing the products. Due to these reasons, our solution and product are available to a larger community base which allows it to be more accessible to amputees. 
                    In the long run, We aim to create a niche specialized technical company that caters to creating human robotics at a lower cost and adapted to the Indian environment. As a venture, we envision to create a budding sector of the industry which reaches out to all over India and provides industrial robotics aids for the human body.
                    """,
            'date': '19-July-2018',
            'image': '/static/images/avatars/user-05.jpg',
            'cover': '/static/images/pointing_gloss.jpg'
        },
        {
            'id':2,
            'author':'Simran Siddharth',
            'title':'A Low-Cost, Open-Source, Compliant Hand for People with Transradial Amputations',
            'body': """An experimental research that took place in the UIUC College of Fine and Applied Arts Creative Research, Illinois made an impressive study. They put forward a design and implementation of a low-cost, open-source prosthetic hand. This prosthetic enables both motor control and sensory feedback for people with transradial amputations. It does so by combining, electromyographic pattern recognition for motor control along with contact reflexes and sensory substitution to provide feedback to the user. The entire hand can be financed for $550, hence is more affordable for researchers and amputees alike. Moreover, the hand is easily integrated into standard sockets, enabling long-term testing.

                    The hardware was compartmentalized into three subsystems: 1) the socket, 2) the hand, and 3) the sensory substitution system. 
                    First, the socket collects and filters data from the residual limb of the user and sends it to the pattern recognition classifier. The hand then stimulates the grasp along with the readings of the pressure sensors in the fingertips of three fingers. In addition, the hand receives pressure readings from the three pairs of pressure sensors located in the fingertips. The research team used an electrotactile stimulation system that is used to provide feedback to the user about contact forces. Compared to the previous design, the entire hand has been mechanically redesigned to be smaller, more vigorous and energy efficient.

                    To evaluate the effectiveness of their motor control and sensory feedback systems, one experiment was performed with a 39-year-old male subject with a right traumatic transradial amputation. The experiment performed involved
                    1) grasping an eggshell without cracking it
                    The subject performed the experiment with his standard industry issued prosthetic arm, as well as the new hand the team at UIUC had developed. Visual feedback was removed with the use of a blindfold. In the eggshell grasping task, the subject attempted to grasp a hollow egg held from his unimpaired left hand to his prosthetic hand. Experiment was repeated ten times. The number of times the eggshell cracked upon grasping was recorded
                    When using his original prosthesis, the subject cracked six eggs and eight eggs when visual feedback was available and then removed, respectively and no eggs were cracked in both visual and no visual feedback conditions in case of the new prosthetic.  

                    Authors describe the advantage of stimulation feedback to be the improvement of the embodiment of the prosthesis. This design is cheap to build and is open source. The use of contact reflexes and sensory substitution improved the grasping of delicate objects like eggshells, when compared to standard myoelectric prostheses

                    """,
            'date':'21-Sept-2018',
            'image': '/static/images/avatars/user-06.jpg',
            'cover': '/static/images/holding.jpg'
        }
    ]
    return articles

form = {}
def add_form(name,mail,subject,message):
    form[name] = [mail,subject,message]
    return True
