from rest_framework import serializers

# Models
from administration.models import Poll

from publicpoll.taskapp.tasks import update_statistics

class PollModelSerializer(serializers.ModelSerializer):
    """Poll with question model serializer ."""
    class Meta:
        """Meta class."""
        model = Poll
        fields = ('name',
                   'question0',
                   'question1',
                   'question2',
                   'question3',
                   'question4',
                   'question5',
                   'question6',
                   'question7',
                   'question8',
                   'question9',
                   )

class AnswerModelSerializer(serializers.Serializer):
    """Serializer of the answers"""
    answer0 = serializers.BooleanField()
    answer1 = serializers.BooleanField(required=False)
    answer2 = serializers.BooleanField(required=False)
    answer3 = serializers.BooleanField(required=False)
    answer4 = serializers.BooleanField(required=False)
    answer5 = serializers.BooleanField(required=False)
    answer7 = serializers.BooleanField(required=False)
    answer6 = serializers.BooleanField(required=False)
    answer8 = serializers.BooleanField(required=False)
    answer9 = serializers.BooleanField(required=False)


    def validate(self, data):
        """All questions must be answered"""
        poll = self.context["poll"]
        if poll.question0 and data.get("answer0") is None:
            raise serializers.ValidationError("Missing answer on question 1")
        if poll.question1 and data.get("answer1") is None:
            raise serializers.ValidationError("Missing answer on question 2")
        if poll.question2 and data.get("answer2") is None:
            raise serializers.ValidationError("Missing answer on question 3")
        if poll.question3 and data.get("answer3") is None:
            raise serializers.ValidationError("Missing answer on question 4")
        if poll.question4 and data.get("answer4") is None:
            raise serializers.ValidationError("Missing answer on question 5")
        if poll.question5 and data.get("answer5") is None:
            raise serializers.ValidationError("Missing answer on question 6")
        if poll.question6 and data.get("answer6") is None:
            raise serializers.ValidationError("Missing answer on question 7")
        if poll.question7 and data.get("answer7") is None:
            raise serializers.ValidationError("Missing answer on question 8")
        if poll.question8 and data.get("answer8") is None:
            raise serializers.ValidationError("Missing answer on question 9")
        if poll.question9 and data.get("answer9") is None:
            raise serializers.ValidationError("Missing answer on question 10")
        return data

    def create(self,data):
        """Voter sent his answers and token is deleted"""
        poll = self.context["poll"]
        consult = self.context["consult"]
        if poll.question0:
            update_statistics.delay(poll.pk, 0, data.get("answer0"))
        if poll.question1:
            update_statistics.delay(poll.pk, 1, data.get("answer1"))
        if poll.question2:
            update_statistics.delay(poll.pk, 2, data.get("answer2"))
        if poll.question3:
            update_statistics.delay(poll.pk, 3, data.get("answer3"))
        if poll.question4:
            update_statistics.delay(poll.pk, 4, data.get("answer4"))
        if poll.question5:
            update_statistics.delay(poll.pk, 5, data.get("answer5"))
        if poll.question6:
            update_statistics.delay(poll.pk, 6, data.get("answer6"))
        if poll.question7:
            update_statistics.delay(poll.pk, 7, data.get("answer7"))
        if poll.question8:
            update_statistics.delay(poll.pk, 8, data.get("answer8"))
        if poll.question9:
            update_statistics.delay(poll.pk, 9, data.get("answer9"))
        consult.answered = True
        consult.save()
        return "success"
        #consult = ConsultModel.objects.create(poll = poll, voter = voter, expiration = data['expiration'])
