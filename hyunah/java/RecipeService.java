public class RecipeService {

    private final RecipeRepository recipeRepository;

    public RecipeInfoResponseDto getRecipeInfo(Long recipeId) {

        //1. 클라이언트로부터 받은 recipeId가 유효한지 화인
        Optional<Recipe> recipeData = recipeRepository.findById(recipeId);

        //1-1. recipeData가 null 인 경우 -> recipeId로 조회시 DB에 데이터가 없다는 것이니 유효하지 않다는 것을 말함
        if(recipeData.isEmpty()) {
            throw new RecipeException("유효하지 않은 아이디입니다."); // 관련 errorcode가 있는지 확인
        }
    }
}
