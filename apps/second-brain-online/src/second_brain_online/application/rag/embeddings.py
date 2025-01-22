from functools import cached_property

from langchain_openai import OpenAIEmbeddings

from second_brain_online.config import settings


class EmbeddingModelBuilder:
    """A singleton class that provides OpenAI embeddings model for text vectorization.

    This class implements the Singleton pattern to ensure only one instance of the
    embeddings model is created and reused throughout the application.

    Attributes:
        _model_id: The identifier of the OpenAI embeddings model to use.
        _device: The device (CPU/GPU) on which to run the model.
        __model: The initialized OpenAI embeddings model instance.
    """

    def __init__(
        self,
        model_id: str = settings.TEXT_EMBEDDING_MODEL_ID,
        device: str = settings.RAG_MODEL_DEVICE,
    ) -> None:
        """Initialize the embeddings model builder.

        Args:
            model_id: The identifier of the OpenAI embeddings model to use.
                Defaults to value from settings.TEXT_EMBEDDING_MODEL_ID.
            device: The device to run the model on.
                Defaults to value from settings.RAG_MODEL_DEVICE.
        """
        self._model_id = model_id
        self._device = device

        self.__model = OpenAIEmbeddings(model=self._model_id)

    @property
    def model_id(self) -> str:
        """Get the identifier of the OpenAI embeddings model.

        Returns:
            The model identifier string.
        """

        return self._model_id

    @cached_property
    def embedding_size(self) -> int:
        """Get the dimensionality of embeddings generated by the model.

        Returns:
            The size/dimension of the embedding vectors.
        """

        return 1536

    def get_model(self) -> OpenAIEmbeddings:
        """Get the initialized OpenAI embeddings model instance.

        Returns:
            The OpenAI embeddings model instance.
        """
        return self.__model


def get_embedding_model() -> OpenAIEmbeddings:
    return EmbeddingModelBuilder().get_model()
