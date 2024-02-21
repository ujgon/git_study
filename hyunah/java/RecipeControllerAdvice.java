@RestControllerAdvice
public class RecipeControllerAdvice {

    @ExceptionHandler(RecipeException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public ResponseEntity<String> recipeException(RecipeException e) {
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
    }

}
