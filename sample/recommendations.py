# Sample script for generating recommendations
import json
from bson.objectid import ObjectId
from datetime import datetime
from bson import json_util

# Create a JREX recommendation entry
def create_recommendation(user_id, article_id, prediction_score, algorithm_id):

    jrex_entry = {
        # MongoDB ObjectID
        "_id": ObjectId(),
        "userId": user_id,
        "articleId": article_id,
        "recommendationAlgorithm": algorithm_id,
        "prediction": prediction_score,
        "createdAt": datetime.now()
    }

    return jrex_entry

# Export articles to JSON
def write_recommendations(recommendation_list):

    filename = "recommendation_list.json"
    
    jrex_list = json.dumps(
        recommendation_list, 
        default=json_util.default, 
        indent = 2)
    
    #print(jrex_list)

    try:
        with open(filename, "w") as outfile:
            outfile.write(jrex_list)
        print("Export complete.")

    except:
        print("Export failed.")
        pass

# Create a recommendations for each user
def assign_articles(user_pool, article_pool, algorithm_name):

    recommendation_list = []

    # Assign each user...
    for i in range(0, len(user_pool)):

        prediction_score = 1000

        # ...each article with...
        for j in range (0, len(article_pool)):
            
            # ...a default prediction score.
            prediction_score = prediction_score - j

            jrex_entry = create_recommendation(
                user_pool[i], 
                article_pool[j], 
                prediction_score, 
                algorithm_name)

            recommendation_list.append(jrex_entry)

    return(recommendation_list)

# Create and export sample recommendations
def main():

    user_pool = ["LTuEwG8JKq2wYoKcR", "9cwgrvWwwh7oGKHoC"]
    article_pool = ["65725f877b7cac9e81bb8271", "65725f877b7cac9e81bb8272"]
    
    algorithm_name = "Default Algorithm"

    # Create sample recommendations for all users
    recommendation_list = assign_articles(user_pool, article_pool, algorithm_name)

    # Export recommendation list to JSON
    write_recommendations(recommendation_list)

# Run example
main()
